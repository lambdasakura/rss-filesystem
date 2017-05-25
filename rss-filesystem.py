import os, sys, errno
import threading

from stat import S_IFDIR, S_IFREG
from fuse import FUSE, FuseOSError, Operations
import feedparser

class Directory():

    def __init__(self, name, uid=1000, gid=1000):
        self.child = {}
        self.name = name
        self.gid = 1000
        self.uid = 1000
        self.size = 0
        self.mode = (S_IFDIR | 0o755)

    def __getitem__(self, key):
        if(key in self.child):
            return self.child[key]
        else:
            return None

    def add_child(self, child):
        self.child[child.name] = child

    def attr(self):
        attr = {}
        attr['st_mode']  = self.mode
        attr['st_gid']   = self.gid
        attr['st_uid']   = self.uid
        attr['st_size']  = self.size
        attr['st_atime'] = 0
        attr['st_ctime'] = 0
        attr['st_mtime'] = 0
        attr['st_nlink'] = 1
        return attr

    def child_list(self):
        return [ k for k,v in self.child.items()]

    def is_dir(self):
        return True

class File():
    def __init__(self, name, content, uid=1000, gid=1000):
        self.child = {}
        self.name = name
        self.gid = 1000
        self.uid = 1000
        self.size = 0
        self.mode = (S_IFREG | 0o644)
        self.content = content

    def __getitem__(self, key):
        return None

    def attr(self):
        attr = {}
        attr['st_mode']  = self.mode
        attr['st_gid']   = self.gid
        attr['st_uid']   = self.uid
        attr['st_size']  = len(self.content)
        attr['st_atime'] = 0
        attr['st_ctime'] = 0
        attr['st_mtime'] = 0
        attr['st_nlink'] = 1
        return attr

    def is_dir(self):
        return False


class RSSFilesystem(Operations):
    def __init__(self, root, fsroot):
        self.fd = 5
        self.root = root
        self.fsroot = fsroot

    # Helpers
    # =======
    def _get_entry(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        cur_ent = self.fsroot
        for i in partial.split('/'):
            if(i == ''):
                break
            if(cur_ent[i] is None):
                return None
            else:
                cur_ent = cur_ent[i]

        return cur_ent

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # Filesystem methods
    # ==================
    def access(self, path, mode):
        pass

    def getattr(self, path, fh=None):
        if(self._get_entry(path) is not None):
            attr = self._get_entry(path).attr()
            return attr
        else:
            raise FuseOSError(errno.ENOENT)

    def readdir(self, path, fh):
        entry = self._get_entry(path)
        dirents = ['.', '..']
        if entry.is_dir() == True:
            dirents.extend(entry.child_list())
        for r in dirents:
            yield r

    def readlink(self, path):
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            # Path name is absolute, sanitize it.
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def statfs(self, path):
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)

    def utimens(self, path, times=None):
        raise FuseOSError(errno.EPERM)

    # File methods
    # ============

    def open(self, path, flags):
        self.fd += 1
        return self.fd

    def read(self, path, length, offset, fh):
        entry = self._get_entry(path)
        return entry.content


def update_fsroot(fsroot):
    rss = [{'name': 'NHK', 'url': "http://www3.nhk.or.jp/rss/news/cat0.xml"},
           {'name': 'slashdot', 'url': "http://rss.rssad.jp/rss/slashdot/slashdot.rss"}]
    sites = fsroot['sites']
    for i in rss:
        dir_ent = Directory(name=i['name'])
        rss_dict = feedparser.parse(i['url'])
        sites.add_child(dir_ent)
        for entry in rss_dict.entries:
            dir_ent.add_child(File(name=entry.title,
                                   content=("Title:" + entry.title + "\n\t" + entry.summary + "\n").encode('utf-8')))



def update_thread(fsroot):
    update_fsroot(fsroot)
    t=threading.Timer(60 * 60, update_thread, [fsroot])
    t.start()



def main(mountpoint, root):
    fsroot = Directory(name="root")
    # categories = Directory(name="categories")
    # fsroot.add_child(categories)
    sites = Directory(name="sites")
    fsroot.add_child(sites)

    t = threading.Thread(target=update_thread, args=[fsroot])
    t.daemon = True
    t.start()
    FUSE(RSSFilesystem(root, fsroot), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    mountpoint = sys.argv[1]
    current_dir = os.getcwd()
    main(mountpoint, current_dir)
