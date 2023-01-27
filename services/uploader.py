class Uploader:

    @staticmethod
    def upload_images_to_movies(instance, filename):
        return f"movies/{instance.slug}/{filename}"

    @staticmethod
    def upload_images_for_cast(instance, filename):
        return f"cast/{instance.slug}/{filename}"
