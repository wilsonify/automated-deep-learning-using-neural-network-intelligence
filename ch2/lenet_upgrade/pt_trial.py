import os
import sys
import nni

# We use relative import for user-defined modules
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../..'
sys.path.append(SCRIPT_DIR)

from ch2.lenet_upgrade.pt_lenet_upgrade_model import PtLeNetUpgradeModel


def trial(hparams):
    """
    Trial Script:
      - Initiate Model
      - Train
      - Test
      - Report
    """
    use_dropout = bool(hparams['dropout']['_name'])
    model_params = {
        "filter_size": hparams['filter_size'],
        "kernel_size": hparams['kernel_size'],
        "l1_size":     hparams['l1_size'],
        "activation":  hparams['activation'],
        "use_dropout": use_dropout
    }
    if use_dropout:
        model_params['dropout_rate'] = hparams['dropout']['rate']

    model = PtLeNetUpgradeModel(**model_params)

    model.train_model(
        batch_size = hparams['batch_size'],
        learning_rate = hparams['learning_rate']
    )
    accuracy = model.test_model()
    nni.report_final_result(accuracy)


if __name__ == '__main__':
    # Manual HyperParameters
    hparams = {
        'dropout':       {'_name': 1, 'rate': 0.5},
        'activation':    'relu',
        'filter_size':   32,
        'kernel_size':   3,
        'l1_size':       64,
        'batch_size':    512,
        'learning_rate': 1e-3,
    }

    # NNI HyperParameters
    # Run safely without NNI Experiment Context
    nni_hparams = nni.get_next_parameter()
    hparams.update(nni_hparams)

    trial(hparams)
