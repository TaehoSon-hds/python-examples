inputs: final: prev: with final;
{

  mypython = python310.withPackages (p: with p; [
    python-lsp-server

    numpy
    pandas
    matplotlib
    scikit-learn
    jupyterlab
  ]);

}
