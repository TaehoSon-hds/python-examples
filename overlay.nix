inputs: final: prev: with final;
{

  mypython = python310.withPackages (p: with p; [
    python-lsp-server
    flake8

    numpy
    pandas
    matplotlib
    scikit-learn
    jupyterlab
  ]);

}
