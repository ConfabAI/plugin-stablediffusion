from ..models.abstract_image_pipeline import AbstractImagePipeline

class PipelineManager:
    def __init__(self):
        self._pipelines = {}
    
    def get_pipeline(self, model_name):
        pipeline = self._pipelines.get(model_name)
        if pipeline is None:
            raise ValueError(f"Pipeline for model {model_name} not found.")
        return pipeline

    def load_pipeline(self, model_dir, model_name):
        if model_name not in self._pipelines:
            self._pipelines[model_name] = AbstractImagePipeline(model_dir, model_name)

pipeline_manager = PipelineManager()