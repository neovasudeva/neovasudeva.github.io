from os import listdir
from os.path import isfile, join
import json
import functools
import shutil

# globals
path_to_index = './src/index'
path_to_projects = './src/projects'
path_to_blogs = './src/blogs'
path_to_templates = './templates'
path_to_build = './build'
path_to_assets = './assets'

## Functions for generating index.html ##
# parses projects directory and returns project html
def generate_projects_html():
    # get projects
    projects = [f for f in listdir(path_to_projects) if isfile(join(path_to_projects, f))] 
    projects = list(filter(lambda x: x[x.rindex('.')+1:] == "json", projects))

    # read each project's json and add to projects_html
    projects_html = []
    for p in projects:
        with open(join(path_to_projects, p), 'r') as p_json:
            p_json_dict = json.loads(p_json.read())
            p_html = \
                "<h2> " + p_json_dict["title"] + " </h2>\n" + \
                "<h5> finished " + p_json_dict["date"] + " </h5>\n" + \
                "<h4> " + p_json_dict["proj_summary"] + " </h4>\n" + \
                "<a href=\"" + p_json_dict["gh_link"] + "\">read more</a>" 
            projects_html.append(p_html)

    # surround each project with div
    projects_html = list(map(lambda x: "<div class=\"proj_entry\">\n" + x + "\n</div>", projects_html))
    projects_html.insert(0, "<p> some of my projects </p> ")

    return projects_html

# parses blogs directory and returns blog html
def generate_blogs_html():
    # get blogs
    blogs = [f for f in listdir(path_to_blogs) if isfile(join(path_to_blogs, f))] 
    blogs = list(filter(lambda x: x[x.rindex('.')+1:] == "json", blogs))

    # read each project's json and add to projects_html
    blogs_html = []
    for b in blogs:
        with open(join(path_to_blogs, b), 'r') as b_json:
            b_json_dict = json.loads(b_json.read())
            b_html = \
                "<h2> " + b_json_dict["title"] + " </h2>\n" + \
                "<h5> finished " + b_json_dict["date"] + " </h5>\n" + \
                "<h4> " + b_json_dict["blog_summary"] + " </h4>\n" + \
                "<a href=\"" + b_json_dict["blog_link"] + "\">read more</a>" 
            blogs_html.append(b_html)

    # surround each project with div
    blogs_html = list(map(lambda x: "<div class=\"blog_entry\">\n" + x + "\n</div>", blogs_html))
    blogs_html.insert(0, "<p> a little blog </p> ")

    return blogs_html

# combine index template and blog/projects html to form index.html
def generate_index_html():
    # STEP 1: parse index.json and replace {{}} occurrences
    index_json_dict = {}
    with open(join(path_to_index, 'index.json'), 'r') as index_json:
        index_json_dict = json.loads(index_json.read())
    
    index_txt = ""
    with open(join(path_to_templates, 'index.html'), 'r') as tindex_html:
        index_txt = tindex_html.read()
        for k in index_json_dict.keys():
            index_txt = index_txt.replace("{{" + k + "}}", index_json_dict[k])
            
    # STEP 2: replace [[content]]
    projects_html = generate_projects_html()
    projects_html_reduce = functools.reduce(lambda a,b: a + '\n' + b, projects_html) 
    blogs_html = generate_blogs_html()
    blogs_html_reduce = functools.reduce(lambda a,b: a + '\n' + b, blogs_html) 
    index_txt = index_txt.replace("[[content]]", projects_html_reduce + blogs_html_reduce)

    return index_txt

if __name__ == '__main__':
    index_txt = generate_index_html()

    # write all files to build directory
    with open(join(path_to_build, 'index.html'), 'w') as index_html:
        index_html.write(index_txt)