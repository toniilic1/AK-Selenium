from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class AllKeySales:
    def KeySales(game):
        
        myOptions = ChromeOptions()
        myOptions.add_argument('start-maximized')
        myOptions.add_argument('--lang=en-GB')
        myOptions.headless = True
        #myOptions.add_experimental_option('detach', True)
        myOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    
        driver = Chrome(options=myOptions)
        driver.set_window_size(1920, 1080)

        driver.get(f'https://www.allkeyshop.com/blog/catalogue/search-{game}')

        searchgame = driver.find_element(By.CLASS_NAME, "search-results-row-link")
        searchgame.click()

        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        info = soup.find(class_="offers-table x-offers")

        topList = []

        buyerName = [games.get_text() for games in info.find_all(class_="x-offer-merchant-name offers-merchant-name")]
        buyerPrice = [games.get_text() for games in info.find_all(class_="x-offer-buy-btn-in-stock")]
        del buyerPrice[2::2]

        for i in range(len(buyerName)):
            topList.append(buyerName[i])
            i += 1
            topList.append(buyerPrice[i])

        getGames = {'{}'.format(i): e for i, e in enumerate(zip(*[iter(topList)]*2), 1)}
        
        curr_url = driver.current_url
        print("Current game URL: \n" + curr_url)
        
        driver.quit()

        return getGames


if __name__ == "__main__":

    serached = input("Enter game name: ")

    sales = AllKeySales.KeySales(serached)

    for key, value in sales.items() :
        print (key, value)
