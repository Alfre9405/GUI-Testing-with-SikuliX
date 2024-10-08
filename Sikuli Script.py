click("1728325847746.png")#Click Search bar Windows
click("1728325620039.png") #look for Chrome App
click ("1728325646069.png")#Choose Chrome Profile
wait(2)  # Wait for the browser to load
type("https://www.adidas.com/us" + Key.ENTER)
wait(2)  # Wait for the page to load
click("1728330478840.png")  # look for the search bar
wait(2)
type("mens sneakers" + Key.ENTER)  # Enter a product name
wait(2)  # Wait for search results to load
if exists("1728344034902.png"):  # Image of the search results header
    print("Search results displayed.")
else:
    print("Search results not found.")
wait(2)
type(Key.PAGE_DOWN*1) # scroll down 1 time
click ("1728344911287.png") # Image of the product in the results
wait(2)
type(Key.PAGE_DOWN*1) # scroll down 1 time
click ("1728331067027.png") #choose the size
wait(2)
click ("1728329840252.png") #click button Add to Bag
if exists("1728329927799.png"):  # Image of the search results header
    print("Correct size selected")
else:
    print("Incorrect size selected.")
wait(4)
click("1728330578437.png") #Click View Bag button