import sys
import tensorflow as tf
import time
import os





import os
image_paths=[]



for dirpath,_,filenames in os.walk(r".\darkpic"):
    filenames.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    for f in filenames:
        image_paths.append( os.path.abspath(os.path.join(dirpath, f)))


print(image_paths)

# change this as you see fit



for image_path in image_paths[100:120]:
    print(image_path)
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                    in tf.gfile.GFile("./labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("./output.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        
        human_string = label_lines[0]
        score = predictions[0][0]
        score =score +0.1

        print('%s (score = %.5f)' % (human_string, score))
        file=open("dark_result.txt","a")
        file.write(str(score)+"\n")
        file.close()

