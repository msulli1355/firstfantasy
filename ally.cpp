#include "ally.h"


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
