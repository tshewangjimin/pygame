
import unittest
import pygame
from pygame.math import Vector2

class SNAKE:
   def __init__(self):
       self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
       self.direction = Vector2(0,0)
       self.new_block = False

   def draw_snake(self):
       pass
   
   def move_snake(self):
       pass

   def add_block(self):
       self.new_block = True

   def reset(self):
       self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
       self.direction = Vector2(0,0)

class TestSNAKE(unittest.TestCase):
   def setUp(self):
       self.snake = SNAKE()

   def test_add_block(self):
       self.snake.add_block()
       self.assertTrue(self.snake.new_block)

   def test_move_snake(self):
       self.snake.move_snake()
       # Add your assertions here

   def test_reset(self):
       self.snake.reset()
       self.assertEqual(self.snake.body, [Vector2(5,10),Vector2(4,10),Vector2(3,10)])
       self.assertEqual(self.snake.direction, Vector2(0,0))
import random

cell_number = 10 # or any other value you want to use

class FRUIT:
  def __init__(self):
      self.randomize()

  def draw_fruit(self):
      fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
      screen.blit(apple,fruit_rect)

  def randomize(self):
      self.x = random.randint(0,cell_number - 1)
      self.y = random.randint(0,cell_number - 1)
      self.pos = Vector2(self.x,self.y)

class TestFRUIT(unittest.TestCase):
  def setUp(self):
      self.fruit = FRUIT()

  def test_randomize(self):
      self.fruit.randomize()
      self.assertTrue(0 <= self.fruit.x <= cell_number - 1)
      self.assertTrue(0 <= self.fruit.y <= cell_number - 1)
      self.assertEqual(self.fruit.pos, Vector2(self.fruit.x, self.fruit.y))

  def test_draw_fruit(self):
      # Add your assertions here
      pass


if __name__ == '__main__':
   unittest.main()