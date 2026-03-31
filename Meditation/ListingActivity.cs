
using Microsoft.VisualBasic;

class Listing : Activity
{
List<string> prompts = new List<string>
{
    "List challenges that have helped you grow as a person",
    "List skills you have developed or improved over time",
    "List moments when you stepped outside your comfort zone",
    "List habits you would like to build or strengthen",
    "List things you are grateful for right now",
    "List people who have positively influenced your life",
    "List activities that bring you joy or peace",
    "List accomplishments you feel proud of",
    "List goals you are currently working toward",
    "List dreams or aspirations you hope to achieve someday",
    "List obstacles that challenge you",
    "List actions you can take to move forward in your life",
    "List emotions you have experienced recently",
    "List personal strengths you rely on during difficult times",
    "List lessons you have learned from life experiences"
};


public void ListingActicity()
    {
        Random random = new Random();

        int index = random.Next(prompts.Count);
        string randomPrompt = prompts[index];

        Console.WriteLine($"---{randomPrompt}---");

        DateTime startTime = DateTime.Now;
        DateTime endTime = startTime.AddSeconds(GetDuration());

        while (DateTime.Now < endTime)
        {
            Console.Write(">");
            string input = Console.ReadLine();
        }




    }






}