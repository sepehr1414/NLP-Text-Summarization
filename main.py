from nltk.tokenize import word_tokenize
from extractive_summerization import summarize
from config import init,context_window_limit,input_text,style_text

init()

def measure_length(text):
    # Measure the length of the document in terms of tokens
    tokens = word_tokenize(text)
    return len(tokens)

def compute_target_lengths(length_doc1, length_doc2):
    # Compute target lengths in a proportional way
    target_length_doc1 = int(length_doc1 / (length_doc1 + length_doc2) * context_window_limit)
    target_length_doc2 = context_window_limit - target_length_doc1
    return target_length_doc1, target_length_doc2



def slice_document(document, context_window_size):
    sentences = word_tokenize(document)
    slices = []
    current_position = 0
    while current_position < len(sentences):
        # Extract a slice of sentences within the context window
        current_slice = sentences[current_position:current_position + context_window_size]
        # Collate the sentences into a summary for the current slice
        summary = ' '.join(current_slice)
        slices.append(summary)
        # Move to the next position within the document
        current_position += context_window_size
    return slices

def summerize_slices(slices):
    summerise=[]
    for slice in slices:
        summerise.append(summarize(slice))
    collated_summary = ' '.join(summerise)
    return collated_summary

def summerize_and_collect(input_text,target_length):
    # Repeat the shrinking input document until the summary size is within the context window
    collated_input_summary=input_text
    while measure_length(collated_input_summary)>context_window_limit:
        # Slice according to the context window 
        slices=slice_document(collated_input_summary, target_length)
        # summerize all slices and collect them
        collated_input_summary=summerize_slices(slices)
    return collated_input_summary


def main():
    # Mesure length
    length_doc1 = measure_length(input_text)
    length_doc2 = measure_length(style_text)
    # Compute target lengths
    target_length_doc1, target_length_doc2 = compute_target_lengths(length_doc1, length_doc2)

    # summerize input text
    collected_input=summerize_and_collect(input_text,target_length_doc1)

    # summerize style text
    collected_style=summerize_and_collect(style_text,target_length_doc2)

    # summerize final text
    collect_final=summerize_and_collect(collected_input+collected_style,target_length_doc1 + target_length_doc2)

    print(collect_final)


if __name__ == "__main__":
	main()