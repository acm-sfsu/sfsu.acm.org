Title: Example Article Workflow
Date: 2014-09-13
Author: Tom Spalding
Tags: pelican, blogging about blogs, publishing, workflows
Category: tutorial
Slug: example-article-workflow
Summary: A meta article workflow for new ACM writers! This is an example article post that goes over the basic steps in contributing to the [sfsu.acm.org](http://sfsu.acm.org) blog.

Congratulations all new ACM officers! Welcome new members!

Since, I've handed down the web reigns to [@bestkao](https://github.com/bestkao) yesterday at the pizza social, I thought I'd make another example workflow for a user who is a guest article writer; this means any of you up-and-coming ACM technical writers out there! Doing this without using my beloved [Grunt](http://gruntjs.com/) or our [Makefile](https://github.com/acm-sfsu/sfsu.acm.org/blob/source/Makefile) for example sake.

**First time**

The first time you download the repo, you're going to have to do some basic setup steps.

1. [Fork](https://github.com/acm-sfsu/sfsu.acm.org/fork) the repo. It will likely rename itself to `acm-sfsu.github.io`. I renamed [mine](https://github.com/digitalvapor/sfsu.acm.org) to `sfsu.acm.org` again.
2. If you are working on the template, fork this too. Otherwise, just clone. Our current template is [acm-sfsu/pelican-cait](https://github.com/acm-sfsu/pelican-cait). It goes in `themes/pelican-cait`.
3. Install the [dependencies](The first time you download the repo, you're going to have to do some basic setup steps such as downloading the dependencies). Make sure to make an [issue](https://github.com/acm-sfsu/sfsu.acm.org/issues) if your setup is different so that other people can follow and that the tutorials are updated.
4. Run `pelican` and open the `index.html` or `article-post.html` generated in the `output` folder in your browser of choice. For example, `firefox ~/projects/sfsu.acm.org/output/example-article-workflow.html`. Did you get any errors? No? Great, continue on.
5. The [Pelican docs](http://docs.getpelican.com/en/latest/) are a great source if you need any help.

**Write the article**

1. I write all of my articles using [Markdown](http://daringfireball.net/projects/markdown/syntax), you'll need to install this if you want to use it. Otherwise [reStructuredText](http://docutils.sourceforge.net/rst.html) is supported by default. See [Writing Content](http://docs.getpelican.com/en/latest/content.html).
2. Check out some of the [other articles'](https://github.com/acm-sfsu/sfsu.acm.org/tree/source/content) metadata to see what you should write. At minimum you should use `Title`, `Date`, Author[s]. `Authors` is a comma-separated list of article authors, otherwise use `Author`.
3. Write that article!!! I like to use [Atom](https://atom.io/) because it has a default plugin that you can just type `ctrl+shift+m` and preview a page in Markdown.

**Commit your code**

After saving...

1. `git add -A` to add all your changes.
2. Then `git commit -m 'adds my article'`.
3. `git push origin source`, where source is our branch that all our code is in.
4. Make a [pull request](https://github.com/acm-sfsu/sfsu.acm.org/pulls) for your article!
5. Your article will then be merged by the [ACM Github Org](people)'s [Web Team](https://github.com/orgs/acm-sfsu/teams/web).

There are probably going to be a lot of tutorials in the future, so besides making an article; a [wiki](https://github.com/acm-sfsu/sfsu.acm.org/wiki), [readme](https://github.com/acm-sfsu/sfsu.acm.org/blob/source/readme.md) update, or a `tutorial` [label](https://github.com/acm-sfsu/sfsu.acm.org/labels) might be the consensus for such things. It is up to you. I put this in the [tutorial category](http://sfsu.acm.org/category/tutorial.html), `Category: tutorial`.

This is a great way for you to get acquainted with [Git](http://git-scm.com/), social coding, and is something you can add to your resume! It is also just fun. :) I encourage all of you to contribute on any topic that interests you, this is your club.

Have a great semester everyone!

Cheers,
[Tom](https://github.com/digitalvapor)
