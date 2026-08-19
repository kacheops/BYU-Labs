def main():
    data = [{"word":"high","score":1001},{"word":"elementary","score":1000},{"word":"public","score":999},{"word":"secondary","score":998},{"word":"medical","score":997},{"word":"primary","score":996},{"word":"old","score":995},{"word":"private","score":994},{"word":"junior","score":993},{"word":"middle","score":992},{"word":"pre","score":991},{"word":"local","score":990},{"word":"graduate","score":989},{"word":"normal","score":988},{"word":"after","score":987},{"word":"modern","score":986},{"word":"english","score":985},{"word":"senior","score":984},{"word":"preparatory","score":983},{"word":"french","score":982},{"word":"rural","score":981},{"word":"technical","score":980},{"word":"parochial","score":979},{"word":"out","score":978},{"word":"boarding","score":977},{"word":"classical","score":976},{"word":"vocational","score":975},{"word":"grammar","score":974},{"word":"year","score":973},{"word":"catholic","score":972},{"word":"famous","score":971},{"word":"comprehensive","score":970},{"word":"grade","score":969},{"word":"day","score":968},{"word":"theological","score":967},{"word":"dental","score":966},{"word":"romantic","score":965},{"word":"residential","score":964},{"word":"latin","score":963},{"word":"italian","score":962},{"word":"called","score":961},{"word":"sunday","score":960}]

            # TODO: Add JSON data here

    adjectives = []
    # TODO: Iterate over the data and extract the adjectives for the word and store them in the list variable
    for items in data:
        adjectives.append(items["word"])
    # TODO: Print the list variable, Example of print: Adjectives for the word "word" are: [list of adjectives]
    print()
    print(f"Adjectives for the word School are: {', '.join(adjectives)}")
    print()
if __name__ == '__main__':
    main()


    