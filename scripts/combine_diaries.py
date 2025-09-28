import yaml
import os
import argparse

def load_diaries(diary_dir):
    all_entries = []
    for root, _, files in os.walk(diary_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data:
                        all_entries.append(data)
    # Sort entries by date for consistent output
    all_entries.sort(key=lambda x: x.get('date', ''))
    return all_entries

def filter_diaries(entries, attribute, value):
    return [entry for entry in entries if entry.get(attribute) == value]

def main():
    parser = argparse.ArgumentParser(description='Combine and filter diary entries from a directory.')
    parser.add_argument('--diary-dir', type=str, default='diary', help='Directory containing the diary entries.')
    parser.add_argument('--output-file', type=str, required=True, help='Output file path for the combined entries.')
    parser.add_argument('--filter-attr', type=str, help='Attribute to filter by (e.g., book or target_language).')
    parser.add_argument('--filter-val', type=str, help='Value of the attribute to filter by.')
    
    args = parser.parse_args()

    all_entries = load_diaries(args.diary_dir)
    
    if args.filter_attr and args.filter_val:
        filtered_entries = filter_diaries(all_entries, args.filter_attr, args.filter_val)
        output_data = filtered_entries
        print(f"Filtered {len(filtered_entries)} entries with {args.filter_attr} = '{args.filter_val}'.")
    else:
        output_data = all_entries
        print(f"Combined all {len(all_entries)} entries.")

    with open(args.output_file, 'w', encoding='utf-8') as f:
        yaml.dump(output_data, f, allow_unicode=True, sort_keys=False)
    
    print(f"Output written to '{args.output_file}'.")

if __name__ == "__main__":
    main()
