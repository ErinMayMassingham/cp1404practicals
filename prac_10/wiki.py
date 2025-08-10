import wikipedia

def main():
    while True:
        search_term = input("Enter page title: ")
        if not search_term:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_term, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')

main()