#include "enemy.h"

Enemy::Enemy()
{
   //call Character::loadImage and do some other stuff TBD later
   Character::loadImage("imp.gif"); //TEMP
}

Enemy::~Enemy()
{
   if (eimage != NULL) SDL_FreeSurface(eimage);
}
SDL_Surface* Enemy::getImage()
{
/*     colorkey = SDL_MapRGB(eimage->format, 0, 0, 255);
     SDL_SetColorKey(eimage, SDL_SRCCOLORKEY, colorkey);
      
     esrc.x = 0;
     esrc.y = 0;
     esrc.w = eimage->w;
     esrc.h = eimage->h;
      
      
     edest.x = 0;
     edest.y = 100;
     edest.w = eimage->w;
     edest.h = eimage->h;
*/
     return eimage;
}

