from ._abstract import AbstractScraper
from ._utils import normalize_string


class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return -1

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def tags(self):
    	tags_html = self.soup.findAll('dt', {'itemprop': 'recipeCategory'})

    	return [normalize_string(tag.get_text()) for tag in tags_html]

    def servings(self):
        return normalize_string(self.soup.find('dd', {'itemprop': 'recipeYield'}).get_text())

    def instructions(self):
        instructions_html = self.soup.find('ol', {'class': 'preparation-groups'}).find_all('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

    def picture(self):
        recipe_photo = self.soup.find('div', {'class': "recipe-image-container"}).find('img')
        return recipe_photo['srcset']
