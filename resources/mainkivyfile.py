import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('submitScreen.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    # Init infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)


    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'hello {name}, you like {pizza}, and your favorite color is {color}!')
        #self.add_widget(Label(text=f'hello {name}, you like {pizza}, and your favorite color is {color}!'))

        # Clearing the input
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        



class TestApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    TestApp().run()
    



'''Old Code
        # Style Constants
        TEXT_INPUT_WIDTH = 400
        TEXT_INPUT_HEIGHT = 70

        # Set columns
        self.cols = 1

        # Defaults for the outer gridLayout
        self.row_force_default = True,
        self.row_default_height=70,
        self.col_force_default=True,
        self.col_default_width=400


        # Create a second gridlayout
        # These defaults apply to everything in the gridLayout
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=400)
        self.top_grid.cols = 2

        # Add widget
        self.top_grid.add_widget(Label(text="Name: "))

        # Add Input Box
        self.name = TextInput(multiline = False)
        self.top_grid.add_widget(self.name)



        # Add widget
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))

        # Add Input Box
        self.pizza = TextInput(multiline = False)
        self.top_grid.add_widget(self.pizza)



        # Add widget
        self.top_grid.add_widget(Label(text="Favorite Color: "))

        # Add Input Box
        self.color = TextInput(multiline = False)
        self.top_grid.add_widget(self.color)

        # Add top grid to the app
        self.add_widget(self.top_grid)

        # Submit Button
        self.submit = Button(text="Submit", 
                             font_size = 32,
                             size_hint_y = None,
                             size_hint_x = None,
                             width = 300,
                             height = 100)
        self.submit.bind(on_press=self.press) # Bind the button
        self.add_widget(self.submit)
        


'''