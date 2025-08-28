#Character.py
#contains definition of character class
#Work begins on 2023-03-27

#Start with Java code.  The code works.  Unlikw the derived classes.

#NOTE I am deleting java code as I write the python code that replaces it.
'''
abstract class Character
{
   //Main Character variables
   protected int classNum;

   //Miscellaneous variables
   protected String abilities[], action;
   protected int abilityCount;
   protected int target;
   protected boolean dead = false;
   protected Image currentImage;
   protected boolean flipState = false;

   public int getClassNum ()
   {
      return classNum;
   }
   public void setClassNum (int c)
   {
      classNum = c;
   }
   public String[] getAbilities ()
   {
      return abilities;
   }
/*	public void setAbilities(String ability)
	{
		//Check to add skill
		if ((abilities.length() > 2) && (abilities[2] == "SKILL"))
		{
			a[index] = abilities[2];
			index++;
		}
		else if (ability == "SKILL")
		{
			a[index] = "SKILL";
		}
		abilityCount++;
	}*/

   public int getAbilityCount ()
   {
      return abilityCount;
   }


   
   
   public boolean isDead ()
   {
      return dead;
   }
   public void isDead (boolean d)
   {
      dead = d;
   }

   public int getLevel ()
   {
      return level;
   }
   public void setLevel (int l)
   {
      level = l;
   }
   public void addLevel (int l)
   {
      level += l;
   }
   public void addLevel ()
   {
      level++;
   }
   public void subtractLevel (int l)
   {
      level -= l;
   }
   public void subtractLevel ()
   {
      level--;
   }

   public int getMaxDamage ()
   {
      return maxDamage;
   }
   public int getMinDamage ()
   {
      return minDamage;
   }

   public int getDamage ()
   {
      int result;
      long seed = System.currentTimeMillis ();
      Random rand = new Random (seed);
      result = rand.nextInt (maxDamage - minDamage);
      if (result == 0)
	 result = 1;
      return result;
   }

   public int getTarget ()
   {
      return target;
   }
   public void setTarget (int t)
   {
      target = t;
   }

   public String getAction ()
   {
      return action;
   }
   public void setAction (String a)
   {
      action = a;
   }

   public Image getCurrentImage ()
   {
      return currentImage;
   }
   public abstract void setCurrentImage (int state);

   public boolean flip ()
   {
      return flipState;
   }
   public void flip (boolean f)
   {
      flipState = f;
   }
}
'''
class Character():
    def __init__(self, name, max_HP, max_MP, level):
        self.name = name
        self.max_HP = max_HP
        self.max_MP = max_MP
        self.current_HP = self.max_HP
        self.current_MP = self.max_MP
        self.level = level

    #HP and MP getters and settters
    def get_current_HP(self):
        return self.current_HP
    def set_current_HP(self, current_HP):
        self.current_HP = current_HP
    def get_current_MP(self):
        return self.current_MP
    def set_current_MP(self, current_MP):
        self.current_MP = current_MP

    #xPos and yPos stuff
    def get_x_Pos(self):
        return self.x_Pos
    def set_x_Pos(self, x_Pos):
        self.x_Pos = x_Pos
    def get_y_Pos(self):
        return self.y_Pos
    def set_y_Pos(self, y_Pos):
        self.y_Pos = y_Pos

    
    
    
    







        
        
