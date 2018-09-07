import os
from sklearn.externals import joblib
from django.core.cache import cache


def recognize_digit(predict_img):
    model_cache_key = 'model_cache'
    model_rel_path = "Home/digits_detection_model/model_cache/cache.pkl"

    model = cache.get(model_cache_key)

    if model is None:
        model_path = os.path.realpath(model_rel_path)
        model = joblib.load(model_path)
        #save in django memory cache
        cache.set(model_cache_key, model, None)

    prediction = model.predict(predict_img)
    return prediction
