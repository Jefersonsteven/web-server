from icecream import ic
import store

def run():
    categories = store.get_categories()
    ic(categories)
    
if __name__ == '__main__':
    run()