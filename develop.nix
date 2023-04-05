{ pkgs }: with pkgs; let

in mkShell {
  packages = [
    mypython
  ];
  buildInputs = (with python310Packages;
    [ python-lsp-server
    ]
  ) ++
  [  ];
}
