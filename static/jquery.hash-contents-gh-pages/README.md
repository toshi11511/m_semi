jquery.hash-contents
====================

location.hash に応じタブ、アコーディオン、ツリービュー等でコンテンツを切り替えることができる jQuery プラグイン

- [使い方](http://www.cyokodog.net/blog/hash-contents-doc/)
- [demo](http://cyokodog.github.io/jquery.hash-contents/demo.html) 

## 変更履歴

- v0.4.1
	- 以下理由で useHash パラメータが false で且つ、内部保持してるカレント hashID と location.hash 値が一致した場合、location.hash 値をクリアするようにしました。 
		- useHash パラメータに false を指定すると、自動生成されるナビゲーションリストのクリック時、location.hash 値が変更されなくなる(ブックマークに location.hash を含ませたくない場合に有効)。<br/>一方で利便性を保つため、外部サイトからのリンクで www.hoge.com#demo1 のように location.hash を指定され呼び出された場合、その値に応じたコンテンツが表示される仕様となっている。そのような方法でページが表示された後、reloadHashChange パラメータが true の状態でナビゲーションリストをクリックすると location.hash を保持した状態でページがリロードされるためコンテンツの切り替えが行われなくなってしまう。<br/>今回の仕様変更で外部サイトより呼び出された後、location.hash がクリアされるためこの問題が解決される。 
- v0.4
	- API を変更。
