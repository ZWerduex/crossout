import crossout

if __name__ == "__main__":
    api = crossout.CrossoutDB()
    i = api.item(456)
    print(i.__dict__)