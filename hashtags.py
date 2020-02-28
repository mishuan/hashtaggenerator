import hashtags_config as hc
import hashtags_data as hd
import argparse 
import random


def add_to_hashtags(h_list, hashtags, size):
    c = 0
    tries = 0
    while c < size and tries < 10:
        rc = random.choice(h_list)
        if rc in hashtags:
            tries += 1
            continue
        else:
            hashtags.add(rc)
            c += 1


def gen_hashtags(photo_type, n=25):
    if n > 30:
        return "Maximum number of hastag is 30."

    if photo_type not in hc.TYPE_MAP:
      return f"'{photo_type}' is not a supported category."

    type_map = hc.TYPE_MAP[photo_type]
    hashtags = set()

    # randomly sample from every hashtag list.
    for key, percent in type_map.items():
        count = int(n * percent)
        add_to_hashtags(hd.LIST_MAP[key], hashtags, count)

    # randomly sample for the leftovers from one random hashtag list
    key = random.choice(list(type_map.keys()))
    leftovers = n - len(hashtags)
    add_to_hashtags(hd.LIST_MAP[key], hashtags, leftovers)

    return "\n".join(hashtags)


def main(): 
    parser = argparse.ArgumentParser(description = "A #hashtag generator") 
    parser.add_argument("-t", "--type", type=str, required=True, help="Type of post (ie, portrait, landscape).") 
    parser.add_argument("-n", "--number", type=int, default=25, help="Number of hashtags.") 
    args = parser.parse_args() 
      
    print(gen_hashtags(args.type, args.number))


if __name__ == "__main__": 
    main()
