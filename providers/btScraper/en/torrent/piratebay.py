# -*- coding: utf-8 -*-

from lib import core

class sources:
    def _soup_filter(self, soup):
        return soup.find_all('tr')

    def _title_filter(self, el):
        return el.find_all('a', {'class', 'detLink'})[0].text

    def _info(self, url, torrent, torrent_info):
        el = torrent_info.el
        link = el.find_all('td')[1]
        torrent['magnet'] = link.find_all('a')[1]['href']

        try:
            info = el.find_all('font', {'class':'detDesc'})[0]
            sub_info = info.text[info.text.find('Size') + 5:]
            size = sub_info[:sub_info.find(',')].replace('i', '').replace('&nbsp;', '')
            torrent['size'] = core.source_utils.de_string_size(size)
        except: pass

        try:
            torrent['seeds'] = int(el.find_all('td')[2].text)
        except: pass

        return torrent

    def _get_scraper(self):
        return core.get_scraper(self._soup_filter, self._title_filter, self._info)

    def movie(self, title, year):
        return self._get_scraper().movie_query(title, year)

    def episode(self, simple_info, all_info):
        return self._get_scraper().episode_query(simple_info)
