#ifndef ENEMYPARTY_H
#define ENEMYPARTY_H

#include "party.h"

const int MAXENEMYCOUNT = 12;
class EnemyParty : public Party
{
   public:
      EnemyParty() { enemycount = 0; }
      ~EnemyParty() {}
      void placeEnemies(int);
      void setEnemyCount(int i){enemycount = i;}
      int getEnemyCount (return enemycount;}


      
   private:
      int enemycount; //How many enemies there are in a party.
};
#endif
