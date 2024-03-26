from datasets import load_dataset


def rep_n(string: str):
    return string.replace("\n", "")


def fix_section(section: dict):
    for k, v in section.items():
        if v != None:
            section[k] = v.replace('"', '""')
    return section


num = 300

data_dict = load_dataset("oshizo/japanese-wikipedia-paragraphs")
datasets = data_dict["train"][:num]

print('"id","pageid","revid","title","section","text"')
for i in range(num):
    print(
        f"\"{datasets['id'][i]}\",\"{datasets['pageid'][i]}\",\"{datasets['revid'][i]}\",\"{datasets['title'][i]}\",\"{fix_section(datasets['section'][i])}\",\"{rep_n(datasets['text'][i])}\""
    )
