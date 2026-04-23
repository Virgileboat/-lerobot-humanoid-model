"""Constants/helpers for bipedal_plateform_no_arms."""

from pathlib import Path

from lerobot_humanoid_models._common import get_mjcf_dir, get_model_dir, get_robot_xml

MODEL_NAME = "bipedal_plateform_no_arms"
MODEL_DIR: Path = get_model_dir(MODEL_NAME)
MJCF_DIR: Path = get_mjcf_dir(MODEL_NAME)
ROBOT_XML: Path = get_robot_xml(MODEL_NAME)


def get_assets(meshdir: str) -> dict[str, bytes]:
  from mjlab.utils.os import update_assets

  assets: dict[str, bytes] = {}
  update_assets(assets, MJCF_DIR, meshdir)
  return assets


def get_spec():
  import mujoco

  spec = mujoco.MjSpec.from_file(str(ROBOT_XML))
  spec.assets = get_assets(spec.meshdir)
  return spec
