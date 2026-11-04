# OpenRouter API Setup Guide
## For RAG Bootcamp Students

**Estimated Time:** 5-10 minutes
**Cost:** $5 minimum (covers 5,000+ queries)

---

## What is OpenRouter?

OpenRouter is a unified API that gives you access to 100+ AI models from different providers:
- OpenAI (GPT-4, GPT-3.5)
- Google (Gemini)
- Anthropic (Claude)
- Meta (Llama)
- And many more!

**Why we use it:**
- Pay-as-you-go (no monthly subscriptions)
- Access multiple models with one API key
- Transparent pricing
- Perfect for learning and experimentation

---

## Step-by-Step Setup

### Step 1: Create an Account

1. **Go to:** https://openrouter.ai/

2. **Click** "Sign In" (top right)

3. **Choose your sign-in method:**
   - Google (recommended - fastest)
   - GitHub
   - Email

4. **Follow the prompts** to complete signup

✅ You should now be on the OpenRouter dashboard!

---

### Step 2: Add Credits to Your Account

**You need at least $5 to get started**

1. **Click** on your profile icon (top right)

2. **Select** "Credits" or "Billing"

3. **Click** "Add Credits"

4. **Enter amount:** Minimum $5 (recommended: $5-10 for entire bootcamp)

5. **Payment options:**
   - Credit/Debit Card
   - UPI (for India)
   - Other methods depending on your region

6. **Complete the payment**

✅ You should see your credit balance updated (e.g., "$5.00")

**💡 How long will $5 last?**
- Average query cost: ~$0.001 (one-tenth of a cent)
- $5 = approximately 5,000 queries
- For this bootcamp (4 sessions): $5 is more than enough!

---

### Step 3: Generate Your API Key

1. **Click** on "API Keys" in the left sidebar (or top menu)

2. **Click** "Create Key" or "New API Key"

3. **Optional:** Give it a name
   - Example: "RAG_Bootcamp"
   - Helps you identify it later if you have multiple keys

4. **Click** "Create"

5. **IMPORTANT:** Copy your API key immediately!
   - It looks like: `sk-or-v1-abc123...xyz789`
   - You'll only see it once!
   - Store it safely (see security tips below)

✅ Your API key is ready to use!

---

### Step 4: Test Your API Key (Optional but Recommended)

Before the session, verify your key works:

#### Using curl (Command Line)

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "google/gemini-flash-1.5",
    "messages": [
      {"role": "user", "content": "Say hello!"}
    ]
  }'
```

Replace `YOUR_API_KEY_HERE` with your actual key.

#### Using Python (Recommended)

```python
import requests
import json

api_key = "YOUR_API_KEY_HERE"  # Replace with your key

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "google/gemini-flash-1.5",
        "messages": [
            {"role": "user", "content": "Say hello!"}
        ]
    }
)

print(response.json())
```

**Expected response:** You should see a JSON response with "Hello!" message

✅ If you see a response, your API is working perfectly!

❌ If you get an error, check:
- Is your API key correct?
- Do you have credits in your account?
- Is there a typo in the URL?

---

## Security Best Practices

### ⚠️ NEVER DO THIS:
- ❌ Share your API key publicly
- ❌ Post it on GitHub, Discord, forums
- ❌ Email it to anyone
- ❌ Hardcode it in files you share

### ✅ ALWAYS DO THIS:
- ✅ Keep it in environment variables
- ✅ Use `.env` files (and add to `.gitignore`)
- ✅ Use `getpass()` in notebooks
- ✅ Regenerate if accidentally exposed

### In Google Colab (What we'll use in class):

```python
import os
from getpass import getpass

# This way, your key is never visible on screen
if 'OPENROUTER_API_KEY' not in os.environ:
    os.environ['OPENROUTER_API_KEY'] = getpass("Enter API key: ")
```

### In Local Development:

Create a `.env` file:
```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
```

Load it in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')
```

---

## Understanding Pricing

### How Pricing Works

OpenRouter charges per token (pieces of text):
- **Input tokens:** Text you send (your question + context)
- **Output tokens:** Text the AI generates (the answer)

Different models have different prices.

### Models We'll Use in Bootcamp

| Model | Input Price | Output Price | Best For |
|-------|-------------|--------------|----------|
| **Gemini Flash 1.5** | $0.075/1M | $0.30/1M | Fast responses, practice |
| Llama 3.1 8B | FREE tier | FREE tier | Experimentation |
| Mistral 7B | $0.07/1M | $0.07/1M | Production use |
| GPT-4o Mini | $0.15/1M | $0.60/1M | High quality answers |

**1M tokens ≈ 750,000 words**

### Real Cost Examples

**Typical RAG query:**
- Question: 50 tokens
- Context (retrieved chunks): 800 tokens
- Answer: 150 tokens
- **Total:** 1,000 tokens

**Using Gemini Flash:**
- Input: 850 tokens × $0.075/1M = $0.00006
- Output: 150 tokens × $0.30/1M = $0.00005
- **Total per query: $0.0001** (one hundredth of a cent!)

**Your $5 credit = ~50,000 queries with Gemini Flash!**

---

## Monitoring Your Usage

### Check Your Balance

1. Go to https://openrouter.ai/
2. Click on your profile
3. Select "Credits" or "Usage"

You'll see:
- Current balance
- Usage history
- Cost per model
- Recent requests

### Set Up Alerts (Recommended)

1. Go to Settings
2. Enable "Low balance alert"
3. Set threshold (e.g., $1)
4. You'll get an email when balance is low

---

## Troubleshooting

### Problem: "Invalid API key"

**Solutions:**
1. Check for typos - copy-paste the key
2. Make sure you copied the entire key (starts with `sk-or-v1-`)
3. Try regenerating a new key
4. Verify you're signed in to the correct account

### Problem: "Insufficient credits"

**Solutions:**
1. Check your balance on the dashboard
2. Add more credits ($5 minimum)
3. Wait a few minutes for payment to process

### Problem: "Rate limit exceeded"

**Solutions:**
1. Wait 60 seconds and try again
2. You might be making too many requests too fast
3. Check if someone else is using your key (security issue!)

### Problem: "Model not available"

**Solutions:**
1. Try a different model (e.g., switch to `google/gemini-flash-1.5`)
2. Check OpenRouter's status page: https://status.openrouter.ai/
3. Some models have waitlists - use alternatives

---

## Recommended Models for Learning

### For Session 1 (Learning & Testing):
**google/gemini-flash-1.5**
- Fast responses
- Very cheap
- Good quality
- Perfect for iteration

### For Session 4 (Final Demo):
**openai/gpt-4o-mini**
- Higher quality
- Still affordable
- Impressive for presentations

### For Experimentation (Free!):
**meta-llama/llama-3.1-8b-instruct:free**
- Completely free
- Decent quality
- Great for testing

---

## Getting Help

### OpenRouter Support
- **Documentation:** https://openrouter.ai/docs
- **Discord:** https://discord.gg/openrouter
- **Email:** support@openrouter.ai

### During Bootcamp
- Ask your instructor
- Check with classmates
- Use the troubleshooting guide
- Backup: Instructor has emergency API key

---

## Pre-Session Checklist

Before Session 1, make sure you have:

- [ ] OpenRouter account created
- [ ] At least $5 credits added
- [ ] API key generated and saved safely
- [ ] Tested API key (optional but recommended)
- [ ] Set up low-balance alert
- [ ] Know how to securely use the key in code

---

## FAQ

**Q: Can I get a refund if I don't use all my credits?**
A: No, but credits don't expire! Use them for future projects.

**Q: Can I share my API key with my study partner?**
A: No! Each person should have their own key. Sharing is a security risk.

**Q: What happens if my key is exposed?**
A: Immediately regenerate it on the OpenRouter dashboard. The old key stops working.

**Q: Can I use the free tier models only?**
A: Yes! Try `llama-3.1-8b:free` - no credits needed. But quality is lower.

**Q: How do I switch models?**
A: Just change the `model_name` parameter in your code. We'll practice this in class.

**Q: Is $5 really enough?**
A: Yes! For this bootcamp, even $3 would be sufficient. Most students use less than $2 total.

**Q: Can I use this API for my own projects?**
A: Absolutely! That's the point. Build whatever you want!

---

## Alternative: Using Free Models Only

If you absolutely cannot add credits, you can still participate using FREE models:

### Free Models Available:
- `meta-llama/llama-3.1-8b-instruct:free`
- `google/gemma-2b-it:free`
- Various other free tier models

### Limitations:
- Slower response times
- Lower quality answers
- May have rate limits
- Not all features available

### How to use in code:
```python
llm = ChatOpenAI(
    model_name="meta-llama/llama-3.1-8b-instruct:free",  # Free model
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPENROUTER_API_KEY'],
    temperature=0.1
)
```

---

## Ready for Session 1?

You're all set if you have:
✅ OpenRouter account
✅ API key saved
✅ Credits loaded ($5+)

See you in class! 🚀

**Questions?** Email the instructor or ask in the class chat.

**Pro Tip:** Join the OpenRouter Discord - great community for learning about different models and best practices!
