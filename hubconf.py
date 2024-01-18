from imagebind.models import imagebind_model

def imagebind_huge(pretrained=True):
    model = imagebind_model.imagebind_huge(pretrained=pretrained)
    return model
