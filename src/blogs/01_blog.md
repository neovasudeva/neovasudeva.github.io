
## Objective

I wanted to create a personal site to contain my projects along with the steps I took to create them. I wanted to be able to:

- easily add content
- keep the site simple
- make the site look somewhat nice

## Inspiration and credits

Massive credit to [Supercip971](https://github.com/Supercip971) on github. He (?) has a great [personal blog](https://supercip971.github.io/)
as well as an [article](https://supercip971.github.io/01-how-I-created-this-blog.html) on how he did it.

I used his method of converting markdown and config files to html. I also used the same styling he did (the css file I used is just modified version of his).

## Markdown to html conversion

I used pypandoc to convert markdown to html. It's what Supercip971 used and it's the only library I could find that satisfactorily converted markdown to html.

There is another library called python-markdown, but it does not properly create
html for codeblocks.

## Dynamic html generation

The final html for this site is dynamically generated from:

1. markdown files
2. json configuration files
3. templated html

These 3 sources are fed to a python script, which uses the json and markdown files to fill the templated html. This is better visualized as:

![](assets/img/workings.png)

Let's take a closer look at the templated html and json config files. Throughout the template, there are lines that look like:

```html
<!-- ... html above ... -->
<h1> {{ title }} </h1>
<!-- ... more html ... -->
<p> {{ date }} </p>
<!-- ... html below ... -->
```

"title" and "date" are both keys that are meant to be replaced. Keys are surrounded by double brackets. Here is a corresponding json config file:

```json
{
    "title": "new blog!",
    "date": "2 May 2021"
}
```

Our keys "title" and "date" are defined with values "new blog!" and "2 May 2021" respectively. Given this json config file and templated html, the python script will find keys in the template html and replace them with the values defined in the json file to generate finalized html. Our final html will look like:

```html
<!-- ... html above ... -->
<h1> new blog! </h1>
<!-- ... more html ... -->
<p> 2 May 2021 </p>
<!-- ... html below ... -->
```

## Content sections

Templated html will also have sections that contain:

```html
<!-- ... html above ... -->
[[content]]
<!-- ... html below ... -->
```

where \[\[content\]\] will be replaced with html generated from markdown. For example, this is used for blog article html where the article itself is created in markdown and then converted to html via pypandoc.

## Deployment

I deployed the site with [github actions](https://github.com/marketplace/actions/deploy-to-github-pages).

## Conclusion

It's been a while so my python code is probably trash. However, I'm very satisfied with the result. I've tried many times to create a personal site, but I was never happy with the result.

Now, I have a platform to link projects and talk about how I built them. Moreover, I didn't have to learn some esoteric js framework!