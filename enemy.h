#ifndef ENEMY_H
#define ENEMY_H

#include "character.h"

class Enemy : public Character
{
   public:
      Enemy(); 
      ~Enemy();
      void setCurrentSprite(int) {}
      Uint32 getColorKey() { return colorkey; }
      SDL_Surface* getImage();
   private:
      SDL_Surface *eimage;
      SDL_Rect esrc, edest;
      Uint32 colorkey;
};
#endif
