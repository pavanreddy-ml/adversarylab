from typing import Literal, List, Union, TypeVar, Generic
from . import NoiseGenerator, NoiseGeneratorMeta

import torch
import tensorflow as tf
from torch.nn import functional as F

class AdditiveNoiseGeneratorTF(NoiseGenerator, metaclass=NoiseGeneratorMeta):
    def __init__(self,
                 framework: Literal["torch", "tf"],
                 epsilon: float,
                 scale: List[int] = None,
                 dist: Literal["normal", "uniform"] = "normal"
                 ) -> None:
        self.framework = framework

        if epsilon < 0 or epsilon > 1:
            raise ValueError("Epsilon must be between 0 and 1")

        self.epsilon = epsilon
        self.dist = dist
        self.scale = scale

    def generate(self, 
              shape: List[int]) -> tf.Tensor:
        if self.dist == "normal":
            noise = tf.random.normal(shape)
            noise = tf.clip_by_value(noise, -1, 1) * self.epsilon
        elif self.dist == "uniform":
            noise = tf.random.uniform(shape, minval=-1, maxval=1) * self.epsilon
        else:
            raise ValueError(f"Unsupported distribution: {self.dist}")
        
        if self.scale is not None:
            current_min, current_max = tf.reduce_min(noise), tf.reduce_max(noise)
            target_min, target_max = self.scale
            noise = (noise - current_min) / (current_max - current_min) * (target_max - target_min) + target_min
        
        return noise
    
    def apply_noise(self, sample: tf.Tensor, noise: tf.Tensor) -> tf.Tensor:
        return sample + noise

    def apply_constraints(self, tensor: tf.Tensor, min_val: float = -1.0, max_val: float = 1.0) -> tf.Tensor:
        return tf.clip_by_value(tensor, clip_value_min=min_val, clip_value_max=max_val)


class AdditiveNoiseGeneratorTorch(NoiseGenerator):
    def __init__(self,
                 framework: Literal["torch", "tf"],
                 epsilon: float,
                 scale: List[int] = None,
                 dist: Literal["normal", "uniform"] = "normal"
                 ) -> None:
        self.epsilon = epsilon
        self.dist = dist

        self.scale = scale

    def generate(self, 
                 shape: List[int]
                 ) -> torch.Tensor:
        if self.dist == "normal":
            noise = torch.randn(shape, device='cuda' if torch.cuda.is_available() else 'cpu')
            noise = torch.clamp(noise, -1, 1) * self.epsilon
        elif self.dist == "uniform":
            noise = torch.rand(shape, device='cuda' if torch.cuda.is_available() else 'cpu') * 2 - 1
            noise *= self.epsilon
        else:
            raise ValueError(f"Unsupported distribution: {self.dist}")
        
        if self.scale is not None:
            current_min, current_max = noise.min(), noise.max()
            target_min, target_max = self.scale
            noise = (noise - current_min) / (current_max - current_min) * (target_max - target_min) + target_min
        
        return noise
    
    def apply_noise(self, *args, **kwargs):
        raise NotImplementedError("Apply Noise Not Implemented for Torch")
    
    def apply_constraints(self, *args, **kwargs):
        raise NotImplementedError("Apply Constrains Not Implemented for Torch")


T = TypeVar('T', AdditiveNoiseGeneratorTF, AdditiveNoiseGeneratorTorch)


class AdditiveNoiseGenerator(Generic[T], metaclass=NoiseGeneratorMeta):
    def __init__(self, framework: Literal["torch", "tf"]) -> None:
        self.framework: Literal["torch", "tf"] = framework
