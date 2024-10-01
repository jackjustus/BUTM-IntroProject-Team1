from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):

    # Velocity
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Referencelist property enables us to shorthand
    # Velocity like v.pos, v.x, and v.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Move() will move the ball one step
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos 
    


class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        # Center ball and randomize angle
        self.ball.center = self.center
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def Update(self, dt):
        # Call ball.move & other things
        self.ball.move()

        # Top & Bottom Collisions
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # Sides Collisions
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        


        pass
    pass


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
