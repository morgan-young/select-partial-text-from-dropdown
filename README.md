It's super annoying that Selenium doesn't let you choose a partial text match in a dropdown, so I built a function that does let you.

How to use:

1. Clone the repo.
2. Get the partial_text_dropdown_match.py file and put it in your folder of whatever project you want to select partial text in a dropdown in.
3. Import it into your main selenium file - from partial_text_dropdown_match import select_partial_text_from_dropdown
4. Use it as normal - select_partial_text_from_dropdown(chrome, //*[@id="random_id"]/div[1], "random_text")
5. If you're stuck, check out my youtube video on this - https://www.youtube.com/watch?v=r6eGBNv8tig