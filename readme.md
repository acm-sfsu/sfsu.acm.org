#ACM at SFSU

Feel free to contribute!

See Pelican's [Getting Started](http://docs.getpelican.com/en/3.3.0/getting_started.html) page.

* fork [the repo](https://github.com/acm-sfsu/acm-sfsu.github.io)
* `git clone --recursive https://github.com/<username>/acm-sfsu.github.io.git`
  * `cd acm-sfsu.github.io`
  * fork the [acm-sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait) theme.
  * `git clone https://github.com/<username>/pelican-cait.git themes/pelican-cait/`
* improve stuff, or write a post/article
  * `make post` or `make page`
  * test locally with `pelican` or `make html`
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
* [Issue #8](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/8).

See [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery).

###Github Activity
* [gha.html](https://github.com/acm-sfsu/pelican-cait/blob/master/templates/gha.html)

See [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity).

###Gravatar
See [pelican-plugins/gravatar](https://github.com/getpelican/pelican-plugins/tree/master/gravatar).

###Share Post
> `share_post` creates old school URLs for some popular sites [...] these links do not have the ability to track the users.

See [pelican-plugins/share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post).

##Metadata

`Template:` - (from [acm/sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait) takes) `contact`, `landing`, (from [pelican-plugins/gallery](https://github.com/getpelican/pelican-plugins/tree/master/gallery) takes) `gallery` for [pages](https://github.com/getpelican/pelican-plugins/tree/master/gallery#gallery-page).

`Gallery:` - [album_name](https://github.com/getpelican/pelican-plugins/tree/master/gallery#articles), example: `Gallery: 2014/02/21`. At the moment this must be paired with `Template: album`, see [issue #8](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/8).

`Modified:` - see [issue #2](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/2).

`Authors:` - see [issue #3](https://github.com/acm-sfsu/acm-sfsu.github.io/issues/3).

`Status:` - `hidden` for pages, `draft` for articles.

##Dependencies
If using [pelican-plugins/github_activity](https://github.com/getpelican/pelican-plugins/tree/master/github_activity) will need [feedparser](https://pypi.python.org/pypi/feedparser). Get with `pip install feedparser`.

If using [pelican-plugins/share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post) need `beautifulsoup4`. Get with `pip install beautifulsoup4`.

If working on theme's CSS, will need [Sass](https://github.com/nex3/sass). Get with `gem install sass`.

##A couple extra dev notes
**Output:**
* `git checkout source` - ensure on `source` branch
* `pelican -d` - deletes output dir and regenerates output into default output directory.
* `git checkout master` - move to master branch. it is your choice whether to persist commits through this master branch or delete it, and make an orphaned branch each time. 
* `cd output`
* `rsync -r --del * ../` recursively move the contents of output directory to main directory and delete the original contents.
* `cd ..`
* `rm -rf output` - remove the output directory
* `git add .` - add everything
* `git commit -m 'generated output'`
