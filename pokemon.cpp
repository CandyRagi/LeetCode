#include<iostream>

using namespace std;

 

class pokemon
{   

    private:
        string name;
        string type;
        int age;
    public:

        pokemon(string name)
        {
            this->name=name;
        }    
        void setName(string name)
        {   
            this->name=name;
        }
        string getName()
        {   
            return this->name;
        }


};

class pikachu:pokemon
{
    private: 
        int power=0;
};

int main()
{

    pokemon x= pokemon("ansh");
    cout<<x.getName();



    return 0;
}