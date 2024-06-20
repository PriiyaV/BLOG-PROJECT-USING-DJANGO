from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand 
import random

class Command(BaseCommand):
    help= "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        #deleting existing data
        Post.objects.all().delete()

        titles=[
            "Boosting Productivity: Tips and Tricks",
            "Finding Balance: Work-Life Harmony Solutions",
            "Effective Communication: Strategies for Success",
            "Mindfulness Meditation: Beginner's Guide",
            "Unlocking Creativity: Inspiring Tips",
            "Self-Care: Making Time for You",
            "Building Resilience: Bouncing Back Stronger",
            "Science of Happiness: Fulfilling Life Strategies",
            "Overcoming Procrastination: Actionable Tips",
            "Embracing Change: Thriving in Uncertainty",
            "Mastering Time Management: Efficient Day Tactics",
            "Cultivating Gratitude: Joyful Living Practices",
            "Healthy Habits: Keys to Happy Living",
            "Power of Mindset: Shaping Your Reality",
            "Stress Management: Calm Mind Techniques",
            "Finding Passion: Pursuing What Matters",
            "Art of Decision Making: Confident Choices",
            "Emotional Intelligence: Success in Life",
            "Living with Purpose: Meaningful Life Discovery"
        ]

        contents = [
            "Tips for creating a productive environment and managing your time effectively: Organize your workspace to minimize distractions. Set specific goals and break tasks into smaller steps. Use time-blocking techniques to allocate time for different tasks. Prioritize tasks using methods like the Eisenhower Matrix. Take regular breaks to maintain focus and avoid burnout.",
            "Strategies for balancing work commitments with personal life: Set clear boundaries between work and personal time. Schedule personal activities just as you would work tasks. Delegate tasks when possible to lighten your workload. Communicate your boundaries to colleagues and family. Practice self-compassion and avoid overcommitting.",
            "Communication techniques for expressing yourself clearly and empathetically: Use 'I' statements to express your feelings without blaming others. Practice active listening to understand the speaker’s perspective. Maintain open body language to show engagement. Clarify and summarize what you’ve heard to ensure understanding. Express empathy by acknowledging others’ feelings and viewpoints.",
            "Introduction to mindfulness meditation and how it can reduce stress: Start with short, guided mindfulness sessions daily. Focus on your breath to anchor your attention. Observe your thoughts without judgment or attachment. Gradually increase the duration of your meditation practice. Notice the calming effects on your mind and body over time.",
            "Exercises and practices to stimulate creativity and overcome creative blocks: Engage in brainstorming sessions without self-censorship. Try new activities or hobbies to inspire fresh ideas. Practice free writing to unlock spontaneous thoughts. Take breaks to allow your mind to rest and reset. Collaborate with others to gain different perspectives.",
            "Ideas for self-care activities to prioritize your mental and physical well-being: Schedule regular physical exercise that you enjoy. Engage in hobbies or activities that bring you joy. Practice relaxation techniques like yoga or deep breathing. Ensure you get adequate sleep and rest. Connect with friends and loved ones for emotional support.",
            "Resilience-building exercises to help you bounce back from setbacks: Reflect on past challenges and how you overcame them. Develop a positive mindset by focusing on solutions. Set realistic goals and celebrate small achievements. Build a support network of friends, family, or mentors. Practice self-compassion and learn from your experiences.",
            "Scientifically proven methods for increasing happiness and life satisfaction: Practice gratitude by keeping a daily journal of things you're thankful for. Engage in regular physical exercise to boost endorphins. Foster social connections and spend quality time with loved ones. Pursue activities that align with your values and passions. Volunteer or help others to experience the joy of giving.",
            "Practical steps to overcome procrastination and boost productivity: Break tasks into smaller, manageable parts to reduce overwhelm. Set specific deadlines and hold yourself accountable. Use tools like to-do lists or productivity apps. Eliminate distractions by creating a focused work environment. Reward yourself for completing tasks to stay motivated.",
            "Adapting to change and embracing new opportunities for personal growth: Keep an open mind and be willing to learn new things. View challenges as opportunities for growth and development. Set flexible goals that can adapt to changing circumstances. Seek feedback and use it constructively to improve. Surround yourself with supportive and positive influences.",
            "Time management techniques to maximize your efficiency and productivity: Prioritize tasks based on urgency and importance. Use time management tools like calendars and planners. Avoid multitasking to improve focus and quality of work. Set specific time limits for tasks to avoid perfectionism. Regularly review and adjust your schedule for optimal efficiency.",
            "Ways to cultivate gratitude and appreciate the positive aspects of life: Keep a gratitude journal and write down things you are thankful for. Express appreciation to others regularly. Focus on the present moment and savor positive experiences. Practice mindfulness to become more aware of everyday blessings. Reflect on positive aspects of your day before going to bed.",
            "Tips for maintaining a healthy lifestyle through diet, exercise, and self-care: Follow a balanced diet rich in fruits, vegetables, and whole grains. Incorporate regular physical activity into your routine. Stay hydrated by drinking plenty of water. Get enough sleep to support overall health and well-being. Engage in regular self-care activities to manage stress.",
            "Harnessing the power of positive thinking to achieve your goals: Visualize your goals and the steps needed to achieve them. Practice positive affirmations to build self-confidence. Focus on solutions rather than problems. Surround yourself with positive and supportive people. Celebrate your successes and learn from your setbacks.",
            "Stress-relief strategies such as mindfulness, exercise, and relaxation techniques: Practice mindfulness meditation to stay present and reduce stress. Engage in regular physical exercise to release tension. Try relaxation techniques like deep breathing or progressive muscle relaxation. Take breaks and practice self-care to prevent burnout. Find hobbies or activities that help you unwind and relax.",
            "Exploring your passions and finding fulfillment in your interests: Reflect on activities that make you feel happy and engaged. Set aside time to pursue your hobbies and interests. Seek opportunities to learn and grow in your areas of passion. Share your interests with others and build a community. Balance your passions with other responsibilities to maintain harmony.",
            "Tools and strategies for making confident decisions in your personal and professional life: Gather relevant information to make informed decisions. Weigh the pros and cons of each option. Trust your intuition and listen to your inner voice. Seek advice from trusted mentors or peers. Commit to your decision and take action confidently.",
            "Developing emotional intelligence skills to navigate relationships and challenges: Practice self-awareness by recognizing your emotions and triggers. Develop empathy by understanding others’ perspectives and feelings. Improve communication skills to express yourself clearly and listen actively. Manage stress and stay calm in challenging situations. Build strong relationships by being supportive and trustworthy.",
            "Reflecting on your values and goals to live a purpose-driven life: Identify your core values and what matters most to you. Set meaningful goals that align with your values and passions. Regularly review and adjust your goals as needed. Make decisions based on your values and long-term vision. Engage in activities that bring a sense of purpose and fulfillment."
        ]


        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/100/800/400",
            "https://picsum.photos/id/1000/800/400",
            "https://picsum.photos/id/1001/800/400",
            "https://picsum.photos/id/1002/800/400",
            "https://picsum.photos/id/1003/800/400",
            "https://picsum.photos/id/1004/800/400",
            "https://picsum.photos/id/1005/800/400",
            "https://picsum.photos/id/1006/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/1008/800/400",
            "https://picsum.photos/id/1009/800/400",
            "https://picsum.photos/id/101/800/400",
            "https://picsum.photos/id/1010/800/400",
            "https://picsum.photos/id/1011/800/400",
            "https://picsum.photos/id/1012/800/400",
            "https://picsum.photos/id/1013/800/400",
            "https://picsum.photos/id/1014/800/400",
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting DATA!"))
