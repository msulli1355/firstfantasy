#ifndef ALLYPARTY_H
#define ALLYPARTY_H

#include "party.h"
#include "ally.h"

class AllyParty : public Party
{
   public:
      AllyParty() {}
      ~AllyParty() {}
   private:
      Ally activecharacter[4];
};
#endif
