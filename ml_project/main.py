import logging
import logging.config
import yaml
import os
import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger("main")

@hydra.main(version_base=None, config_path="config", config_name="default")
def main(cfg_dict: DictConfig) -> None:
    logger.debug(OmegaConf.to_yaml(cfg_dict))
    logger.info("Start")
    model = instantiate(cfg_dict.mode, dataloader=cfg_dict.dataloader)
    model()


if __name__ == '__main__':
    main()
