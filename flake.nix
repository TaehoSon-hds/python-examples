{
  description = "python-examples";

  inputs = {

    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";

  };

  outputs =
    inputs@{ self, nixpkgs, flake-utils, ... }:
    {
      overlay = nixpkgs.lib.composeManyExtensions [
                  (import ./overlay.nix inputs)
                ];
    } // flake-utils.lib.eachDefaultSystem (system:

      let
        pkgs = import nixpkgs {
          inherit system;
          config = {};
          overlays = [ self.overlay ];
        };
      in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
                          mypython
                        ];
        };
      }

    );
}
