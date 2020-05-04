import re
import urllib.request
import urllib.parse
import vim
import webbrowser


def get_link(terms):
    query = 'https://duckduckgo.com/html/?q=%5C{}'.format(
        terms.strip().replace(' ', '+')
    )
    response = urllib.request.urlopen(query)
    link = response.getheader('location')

    if not re.match(r'https://duckduckgo\.com/html', link):
        return link


def open_search(terms):
    webbrowser.open('https://google.com/search?q=' + urllib.parse.quote(terms))


# Hooks for calling directly from vimscript.

def _vim_open_search():
    open_search(vim.eval("a:terms"))


def _vim_link_for_terms():
    terms = vim.eval("a:terms")
    link = get_link(terms)
    vim.command("let link_out='{}'".format(link))
