import nltk


input_text = """
The universe is a vast and mysterious space, filled with galaxies, stars, and planets. Scientists have been studying the cosmos for centuries, trying to unravel its secrets. From the Big Bang to the formation of galaxies, there is so much to explore and understand.

In our own solar system, we have eight planets, each with its own unique characteristics. Earth, the third planet from the sun, is teeming with life and diverse ecosystems. The exploration of space has led to incredible discoveries, such as black holes, pulsars, and exoplanets.

Advancements in technology have allowed us to launch satellites, probes, and rovers to explore distant corners of our solar system and beyond. The Hubble Space Telescope has captured stunning images of nebulae, supernovae, and distant galaxies, expanding our understanding of the cosmos.

As we gaze into the night sky, we are reminded of the vastness of the universe and our place in it. The quest for knowledge continues, and astronomers and scientists around the world work together to unlock the mysteries of the cosmos.

Space exploration has not only expanded our scientific understanding but has also inspired wonder and curiosity among people of all ages. The dream of reaching other planets and possibly other star systems fuels the imagination and pushes the boundaries of human exploration.

In the future, as technology advances further, we may witness even more incredible discoveries and perhaps even the exploration of distant exoplanets that could harbor signs of extraterrestrial life. The universe remains an endless frontier, inviting us to explore, learn, and marvel at its beauty and complexity.
"""

style_text = """
Art and creativity have been integral parts of human civilization throughout history. From ancient cave paintings to Renaissance masterpieces, artistic expression has evolved and taken various forms. Today, we live in a world where art surrounds us in many ways, from paintings and sculptures to digital art and multimedia installations.

Art has the power to evoke emotions, provoke thoughts, and challenge societal norms. It serves as a reflection of culture, beliefs, and individual experiences. The diversity of artistic styles and movements allows for a rich tapestry of expression, ranging from realism to abstract and conceptual art.

In the contemporary art scene, artists experiment with new mediums, pushing boundaries and redefining traditional notions of art. Street art, performance art, and interactive installations engage audiences in immersive experiences. The intersection of technology and art has given rise to digital art, virtual reality exhibits, and interactive online platforms.

Art institutions, museums, and galleries play a crucial role in preserving and showcasing artistic achievements. They serve as cultural hubs, bringing communities together to appreciate and celebrate creativity. Art education fosters the next generation of artists, encouraging exploration and innovation.

The role of artists in society goes beyond aesthetics; they are often catalysts for social change, advocates for justice, and storytellers of the human experience. Artistic expression transcends language barriers, connecting people from different backgrounds and fostering a sense of shared humanity.

As we navigate the complexities of the modern world, art continues to be a source of inspiration, offering a lens through which we can explore, question, and appreciate the diversity of the human experience. The journey of artistic expression is ongoing, shaped by the evolving perspectives and voices of artists around the globe.
"""

context_window_limit = 4000

def init():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
        nltk.download("stopwords")