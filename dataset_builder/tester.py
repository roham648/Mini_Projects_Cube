import json
from collections import Counter

def test_my_dataset(filename="dataset.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File {filename} not found!")
        return
    
    print("=" * 50)
    print("🧪 DATASET TEST REPORT")
    print("=" * 50)
    
    # ۱. Basic info
    print(f"📊 Total samples: {len(data)}")
    
    # ۲. Operations distribution
    operations = [item["operation"] for item in data]
    op_counts = Counter(operations)
    print(f"\n🔧 Operations:")
    for op, count in op_counts.items():
        print(f"  {op}: {count} samples")
    
    # ۳. Check for duplicates
    problems = [item["problem"] for item in data]
    unique = set(problems)
    print(f"\n🔄 Uniqueness:")
    print(f"  Unique problems: {len(unique)}")
    print(f"  Duplicates: {len(data) - len(unique)}")
    
    # ۴. Check answer correctness
    print(f"\n✅ Answer verification:")
    errors = []
    for item in data:
        problem = item["problem"]
        expected = int(item["answer"])
        
        # Parse problem
        parts = problem.split()
        if len(parts) == 3:
            num1, op, num2 = int(parts[0]), parts[1], int(parts[2])
            
            if op == "+":
                actual = num1 + num2
            elif op == "-":
                actual = num1 - num2
            
            if actual != expected:
                errors.append(f"{problem} = {expected} (should be {actual})")
    
    if errors:
        print(f"  ❌ Found {len(errors)} errors!")
        for error in errors[:3]:
            print(f"    {error}")
    else:
        print("  ✅ All answers are correct!")
    
    # ۵. Sample display
    print(f"\n🎲 Random samples:")
    import random
    samples = random.sample(data, min(5, len(data)))
    for item in samples:
        print(f"  {item['problem']} = {item['answer']}")
    
    # ۶. Number range
    all_numbers = []
    for item in data:
        parts = item["problem"].split()
        all_numbers.extend([int(parts[0]), int(parts[2])])
    
    print(f"\n📈 Number range:")
    print(f"  Min: {min(all_numbers)}")
    print(f"  Max: {max(all_numbers)}")
    print(f"  Avg: {sum(all_numbers)/len(all_numbers):.1f}")
    
    print("\n" + "=" * 50)
    print("Test completed! 🎉")

# اجرای تست
if __name__ == "__main__":
    test_my_dataset()