#ACM at SFSU

Feel free to contribute!

* fork [the repo](https://github.com/acm-sfsu/acm-sfsu.github.io)
* `git clone --recursive https://github.com/<username>/acm-sfsu.github.io.git`
  * `cd acm-sfsu.github.io`
  * fork the [acm-sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait) theme.
  * `git clone https://github.com/<username>/pelican-cait.git themes/pelican-cait/`
* improve stuff, or write a post/article
  * `make post` or `make page`
  * teset locally with `pelican` or `make html`
  * `git commit -am 'brief but informative message'`
* make a [pull request](https://github.com/acm-sfsu/acm-sfsu.github.io/pulls)!

If you need ideas on where to contribute, check out the [issue list](https://github.com/acm-sfsu/acm-sfsu.github.io/issues)! Put issues related to theming ([acm-sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait)) here too.

If you have any questions, please drop by [#acm-sfsu](http://webchat.freenode.net/?channels=acm-sfsu).

##Make
* `make help` - help

added commands
* `make post` and `make page` - see [issue #4](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/4)
* `make sass` - generates `.css` from `.scss`. Set `THEME_NAME` in `Makefile`. See [Sass](https://github.com/nex3/sass).

##Plugins
Plugins can be added in the `pelicanconf.py` file's `PLUGINS` line.

###Gallery
See [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery).

###Github Activity
See [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity).

###Gravatar
See [pelican-plugins/gravatar](https://github.com/getpelican/pelican-plugins/tree/master/gravatar).

###Share Post
> `share_post` creates old school URLs for some popular sites [...] these links do not have the ability to track the users.

See [pelican-plugins/share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post).

##Metadata

`Template:` - (from [acm/sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait) takes) `contact`, `landing`, (from [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery) takes) `gallery`.

`Modified:` - see [issue #2](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/2).

`Authors:` - see [issue #3](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/3).

`Status:` - `hidden` for pages, `draft` for articles.

##Dependencies
If using [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity) will need [feedparser](). Get with `pip install feedparser`.

If using [pelican-plugins/share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post) need `beautifulsoup4`. Get with `pip install beautifulsoup4`.

If working on theme's CSS, will need [Sass](https://github.com/nex3/sass). Get with `gem install sass`.