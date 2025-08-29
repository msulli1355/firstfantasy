'''#include "ally.h"


Ally::Ally(char* n, int jobclass)
{
   Character::setName(n);
}
Ally::~Ally()
{
}
void Ally::setCurrentSprite(int index)
{
   currentrect->w = 64;
   currentrect->h = 64;
   currentrect->y = 0;
   currentrect->x = index*currentrect->w;
}

bool Ally::advance()
{
   return true; //Ally HAS advanced
}

bool Ally::retreat()
{
   return true; //Ally HAS retreated
}
'''
from character import *
class Ally(character):
   def __init__(self, n, jobclass):
      setName(n)
      self.current_rect = rect()
   def set_current_sprite(self, index):
      self.current_rect.w = 64
      self.current_rect.h = 64
      self.current_rect.y = 0
      self.current_rect.x = index * self.current_rect.y
   def advance():
      return True #Ally has advanced
   def retreat():
      return True #Ally has retreated

