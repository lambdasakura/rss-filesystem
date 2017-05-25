# RSS filesystem

you can rss feeds in file.

## run RSS filesystem

```shell
mkdir rss-filesystem # create mountpoint
python rss-filesystem.py rss-filesystem
```


```shell
$ cd rss-filesystem/sites/                                                                                                                                   [master ~/dev/src/github.com/lambdasakura/rss-filesystem]
NHK/  slashdot/
$ tree .                                                                                                                                                [~/dev/src/github.com/lambdasakura/rss-filesystem/rss-filesystem/sites]
.
├── NHK
│   ├── 「文書は本物」の証言 文科相「コメントする立場にない」
│   ├── 英テロ事件 容疑者の親族ら英とリビアで相次ぎ拘束
│   ├── 元ＫＡＴーＴＵＮの田中容疑者 車内に大麻にも使う巻紙
│   ├── 自衛隊トップの憲法発言 民進など批判 自民「問題ない」
│   ├── 新たに２つ手りゅう弾のような不審物 ＪＲ東飯能駅近く
│   ├── 地割れの幅広がり警報器が作動 大分 豊後大野
│   └── 民進と共産 前次官の国会招致妨げないよう求める
└── slashdot
    ├── 2017年第1四半期のスマートフォン販売台数は3億7,997万台、中国メーカーの増加が続く
    ├── JASRAC、ネット上への歌詞掲載でも「引用」であれば使用料は不要と明言
    ├── NETGEARのルーターで利用統計を収集しメーカーに送信する機能が追加される
    ├── 「Vimを終了する方法」、100万PVを突破
    ├── サイボウズ社員の標準PCはメモリ32GB、NVMe 512GB
    ├── ビットコインの価値が急上昇中
    ├── 自民党、大学の授業料を卒業後に支払える制度を提案
    ├── 政府、「行政に割り当てられているが有効活用されていない周波数帯」を民間開放する方針を示す
    ├── 電子投票機を改ざんできるという主張を受けてインド選挙管理委員会がハッキングコンテストを開催へ
    └── 日立がメインフレームのハードウェア開発から撤退

2 directories, 17 files
```

```shell
$ cat slashdot/自民党、大学の授業料を卒業後に支払える制度を提案                                                                                         [~/dev/src/github.com/lambdasakura/rss-filesystem/rss-filesystem/sites]
Title:自民党、大学の授業料を卒業後に支払える制度を提案
        <p><img align="right" height="64" width="64" src="https://images.srad.jp/topics/money_64.png">あるAnonymous Coward 曰く、実質的には借金に相当する奨学金対し、卒業後の返済滞納などが問題となっている。これに対し自民党の教育再生実行本 部が、「大学などに在学している間は授業料を無償化し、卒業後に収入に応じて国に納付する新たな制度」を提言しているという（NHK）。

単に支払いを遅らせるだけであれば現行の貸与型奨学金とあまり変わらないが、卒業後の収入によって大きく減免される（たとえば無収入や一定以下であれば返済免除など）のであれば検討に値すると思う。<p> <a href="https://srad.jp/story/17/05/25/0449242/">すべて読む</a> | <a href="https://srad.jp/stories/ed">教育</a> | <a href="https://srad.jp/stories/government">政府</a> | <a href="https://srad.jp/stories/money">お金</a> | <a href="https://twitter.com/share?url=https://srad.jp/story/17/05/25/0449242/&amp;text=%E8%87%AA%E6%B0%91%E5%85%9A%E3%80%81%E5%A4%A7%E5%AD%A6%E3%81%AE%E6%8E%88%E6%A5%AD%E6%96%99%E3%82%92%E5%8D%92%E6%A5%AD%E5%BE%8C%E3%81%AB%E6%94%AF%E6%89%95%E3%81%88%E3%82%8B%E5%88%B6%E5%BA%A6%E3%82%92%E6%8F%90%E6%A1%88" title="この記事をTwitterでつぶやく"><img alt="この記事をTwitterでつぶやく" border="0" src="//images.srad.jp/classic/img/twitter_32.png/20150127" /></a> <a href="//www.facebook.com/sharer.php?u=https://srad.jp/story/17/05/25/0449242/" title="この記事をFacebookで共有"><img src="//images.srad.jp/classic/img/facebook_32.png" border="0" alt="この記事をFacebookで共有" /></a> <a href="https://plus.google.com/share?url=https://srad.jp/story/17/05/25/0449242/" title="この記事 をGoogle Plusで共有"><img src="https://www.gstatic.com/images/icons/gplus-32.png" border="0" alt="この記事をGoogle Plusで共有" /></a> <a href="//b.hatena.ne.jp/entry/https://srad.jp/story/17/05/25/0449242/" title="このエントリーをはてなブックマークに追加"><img src="https://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="32" height="32" style="border: none;" border="0" /></a> </p> <p> 関連ストーリー： <br><a href="https://srad.jp/story/16/10/21/0817209">経済的に厳しい大学生への給付型奨学金、高校時の成績を条件とする案が出る</a> <small>2016年10月21日</small> <br><a href="https://srad.jp/story/16/09/01/0458234">文科省、無利子奨学金を基準を満たした 全員に貸与する方針へ</a> <small>2016年09月01日</small> <br><a href="https://srad.jp/story/15/12/22/068245">海外の理系博士課程学生の生活費事情</a> <small>2015年12月22日</small> <br><a href="https://srad.jp/story/15/08/21/0614255">東京理科 大、博士課程の学費を「実質無料」へ</a> <small>2015年08月21日</small> </p></p>
```
