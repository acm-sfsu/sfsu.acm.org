#ACM at SFSU

Feel free to contribute!

* fork the repo
* `git clone --recursive https://github.com/<username>/acm-sfsu.github.io.git`
* improve stuff, or write a post/article
  * `make post` or `make page`
  * `git commit -am 'brief but informative message'`
* make a [pull request](https://github.com/acm-sfsu/acm-sfsu.github.io/pulls)!

If you need ideas on where to contribute, check out the [issue list](https://github.com/acm-sfsu/acm-sfsu.github.io/issues)! Put issues related to theming ([acm-sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait)) here too.

If you have any questions, please drop by [#acm-sfsu](http://webchat.freenode.net/?channels=acm-sfsu).

##Plugins
Plugins can be added in the `pelicanconf.py` file's `PLUGINS` line.

###Gallery
See [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery).

###Github Activity
See [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity).

###Gravatar
See [pelican-plugins/gravatar](https://github.com/getpelican/pelican-plugins/tree/master/gravatar).

###Share Post
See [pelican-plugins/share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post).

##Metadata

`Template:` (from [acm/sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait) takes) `contact`, `landing`, (from [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery) takes) `gallery`.

`Modified:` - see [issue #2](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/2).

`Authors:` - see [issue #3](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/3).

`Status:` - `hidden` for pages, `draft` for articles.

##Dependencies
If using [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity) will need [feedparser](). `pip install feedparser`