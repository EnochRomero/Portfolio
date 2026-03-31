
namespace Develop02
{
    public static class RandomPromptGenerator
    {
        private static List<string> RandomPrompts = new List<string>
        {
            "What was the best part of your day?",
            "What challenged you today?",
            "What are you grateful for right now?",
            "How did you take care of yourself today?",
            "What made you smile today?",
            "What is something you learned today?",
            "What is one thing you could have done better today?",
            "How did you feel emotionally today, and why?",
            "What is something you're proud of today?",
            "Who did you interact with today, and how did it make you feel?",
            "What was the most stressful moment today?",
            "What helped you relax today?",
            "What goal did you work toward today?",
            "What is something you’re looking forward to?",
            "What is one thought you couldn’t stop thinking about today?",
            "How did today compare to yesterday?",
            "What is something you want to remember about today?",
            "What energized you today?",
            "What drained your energy today?",
            "If today had a theme, what would it be?"
        };



        public static string GetRandomPrompt()
        {
            int randomIndex = Random.Shared.Next(RandomPrompts.Count);
            return RandomPrompts[randomIndex];
        }
    }
}