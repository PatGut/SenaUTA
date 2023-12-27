import numpy as np
import tensorflow as tf


class handClassifier(object):
    def __init__(
        self,
        model_path='model/HandClassifier/keypoint_classifier.tflite',
        num_threads=1,
    ):
        self.interpreter = tf.lite.Interpreter(model_path=model_path,
                                               num_threads=num_threads)

        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        print("Detalles de entrada del modelo:", self.input_details)


    def __call__(
        self,
        landmark_list,
    ):
        input_details_tensor_index = self.input_details[0]['index']
        input_data = np.array([landmark_list], dtype=np.float32)
        print("Dimensiones de los datos de entrada:", input_data.shape)
        # Ajusta la forma de los datos de entrada para que coincida con las expectativas del modelo
        nueva_forma = (1, 42)
        input_data = np.array([landmark_list], dtype=np.float32).reshape(nueva_forma)
        print("NUEVAS Dimensiones de los datos de entrada:", input_data.shape)

        self.interpreter.set_tensor(
            input_details_tensor_index,
            input_data)
        self.interpreter.invoke()

        output_details_tensor_index = self.output_details[0]['index']

        result = self.interpreter.get_tensor(output_details_tensor_index)

        result_index = np.argmax(np.squeeze(result))    

        return result_index